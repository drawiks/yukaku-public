
#шаблон создания рассписания
#в ключе можете написать все что хотите
lessons = {
    "meet1":"<ваш ID конференции>",
    "meet2":"ufy-ejck-ges",
    "meet3":"<ваш ID конференции>",
}

#используйте дни недели в формате Monday, Tuesday...
shedule = {
    "Friday":{
            "09:55":lessons["meet1"],
            "12:00":lessons["meet3"],
            "13:05":lessons["meet1"],
            "05:22":lessons["meet2"],
        },
    #...
}
