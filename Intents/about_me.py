from aiogram import types
from loader import dp, bot
from inline_bottons import yes_no, list_yes_no, Specialties, list_specialities, save_info
from bottons import menu_start, menu_main
from aiogram.dispatcher.storage import FSMContext
from Intents.classes import About_me


@dp.message_handler(text='Рассказать о себе')
async def answer(message: types.Message, state: FSMContext):
    await message.answer(text='Давайте познакомимся поближе))', reply_markup=menu_main)
    await message.answer(text='Мне нужно задать вам несколько вопросов, чтобы я мог рассказать о вас. '
                              'После вопросов я покажу, как будет выглядеть информация о вас для других людей. '
                              'Вы всегда сможете ее скорректировать. Поехали?', reply_markup=yes_no)
    await About_me.AB_go.set()


@dp.callback_query_handler(text=list_yes_no, state=About_me.AB_go)
async def answer1(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))

    if text == 'yes':
        await bot.send_message(message.from_user.id, text='Поехали! 1-ый вопрос из 4-х:\n'
                                                          'Как вас зовут? Вы можете написать как только имя, так и '
                                                          'добавить к нему фамилию или отчество. Их будут видеть '
                                                          'другие люди')
        await About_me.AB_name.set()
    else:
        await bot.send_message(message.from_user.id, text='Давайте вернемся в главное меню))\n'
                                                          'Выберете, что вас интересует', reply_markup=menu_start)
        await state.finish()


@dp.message_handler(state=About_me.AB_name)
async def answer2(message: types.Message, state: FSMContext):
    text = message.text
    await message.answer(f'Отлично, запомнил ваше имя - {text}')
    await bot.send_message(message.from_user.id,
                           text='2-й вопрос из 4-х:\nВ какой категории услуг вы можете быть полезным другим людям?',
                           reply_markup=Specialties)
    await About_me.AB_spec.set()


@dp.callback_query_handler(text=list_specialities, state=About_me.AB_spec)
async def answer3(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    await bot.send_message(message.from_user.id,
                           f'Хорошо, запомнил вашу специализацию - {text}')
    await bot.send_message(message.from_user.id,
                           text='3-й вопрос из 4-х:\nСколько стоят ваши услуги? Напишите число и валюту')
    await About_me.AB_price.set()


@dp.message_handler(state=About_me.AB_price)
async def answer4(message: types.Message):
    text = message.text
    await message.answer(f'Замечательно! Вот такую цену я запомнил - {text}')
    await message.answer('Теперь последний 4-ый вопрос - Напишите немного о себе, о своем предложении')
    await About_me.AB_about.set()


@dp.message_handler(state=About_me.AB_about)
async def answer5(message: types.Message):
    text = message.text
    await message.answer(f'Итак, вы ответили на все мои вопросы. Вот, что я о вас сейчас знаю:')
    await bot.send_message(message.from_user.id, text='Все верно?', reply_markup=save_info)
    await About_me.AB_edit.set()


@dp.callback_query_handler(state=About_me.AB_edit)
async def answer6(message: types.Message, state: FSMContext):
    text = str(dict(message).get('data'))
    if text == 'edit':
        await bot.send_message(message.from_user.id, text='Какое поле вы хотите отредактировать?')
    else:
        await bot.send_message(message.from_user.id, text='Отлично! Возвращаемся в главное меню',
                               reply_markup=menu_start)
        await state.finish()
