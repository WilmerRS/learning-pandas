class Logger:
    @classmethod
    def info(
            cls,
            *,
            data,
            title='',
            inline=False,
            header=True,
            finish=True
    ):
        cls.__log(
            data=data,
            title=title,
            emoji='🌀',
            inline=inline,
            header=header,
            finish=finish)

    @classmethod
    def error(
        cls,
        *,
        data,
        title='',
        inline=False,
        header=True,
        finish=True
    ):
        cls.__log(
            data=data,
            title=title,
            emoji='❌',
            inline=inline,
            header=header,
            finish=finish
        )

    @classmethod
    def warn(
        cls,
        *,
        data,
        title='',
        inline=False,
        header=True,
        finish=True
    ):
        cls.__log(
            data=data,
            title=title,
            emoji='⚠️',
            inline=inline,
            header=header,
            finish=finish
        )

    @classmethod
    def __log(cls,
              *,
              data,
              title='',
              emoji,
              inline=False,
              header=True,
              finish=True
              ):
        car = '\n' if not inline else ''
        print(
            f'\n{emoji} Log: {title} {car}' if header else '',
            data,
            f'{car}{emoji} Finish: {title}\n' if finish else ''
        )
