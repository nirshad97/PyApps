import justpy as jp
from webapp import layout
from webapp import page

class About(page.Page):

    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page!",
               classes="text-4xl m-2")
        jp.Div(a=div, text="""In publishing and graphic design, Lorem ipsum is a
                placeholder text commonly used to demonstrate the
                visual form of a document or a typeface without 
                relying on meaningful content. Lorem ipsum may 
                be used as a placeholder before final copy is available.""",
               classes="text-lg px-2")
        return wp