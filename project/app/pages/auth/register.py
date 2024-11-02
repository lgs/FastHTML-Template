from app.components.toaster import add_custom_toast
from project.app.services.auth.auth_service import AuthService
from fasthtml.common import *
from fasthtml.core import APIRouter
from fh_frankenui.core import *
from starlette.responses import RedirectResponse

rt = APIRouter()
auth_service = AuthService()


@rt("/auth/register")
async def get(request):
    left = Div(
        cls="col-span-1 hidden flex-col justify-between bg-zinc-900 p-8 text-white lg:flex"
    )(
        Div(cls=(TextT.bold, TextT.default))("Acme Inc"),
        Blockquote(cls="space-y-2")(
            P(cls=TextT.large)(
                '"This library has saved me countless hours of work and helped me deliver stunning designs to my clients faster than ever before."'
            ),
            Footer(cls=TextT.small)("Sofia Davis"),
        ),
    )

    right = Div(cls="col-span-2 flex flex-col p-8 lg:col-span-1")(
        DivRAligned(
            A(Button("Login", cls=ButtonT.ghost, submit=False), href="/auth/login")
        ),
        DivCentered(cls="flex-1")(
            Div(cls=f"space-y-6 w-[350px]")(
                Div(cls="flex flex-col space-y-2 text-center")(
                    H3("Create an account"),
                    P(cls=TextFont.muted_sm)(
                        "Enter your email below to create your account"
                    ),
                ),
                Form(cls="space-y-6", method="post")(
                    Input(
                        placeholder="name@example.com",
                        name="email",
                        id="email",
                        type="email",
                    ),
                    Input(
                        placeholder="••••••••",
                        name="password",
                        id="password",
                        type="password",
                    ),
                    Button(
                        # Span(cls="mr-2", uk_spinner="ratio: 0.54"),
                        UkIcon("mail", cls="mr-2"),
                        "Sign up with Email",
                        cls=(ButtonT.primary, "w-full"),
                        # disabled=True,
                    ),
                    DividerSplit("Or continue with", cls=TextFont.muted_sm),
                    Button(
                        UkIcon("github", cls="mr-2"),
                        "Github",
                        cls=(ButtonT.default, "w-full"),
                        # uk_toggle="#demo",
                    ),
                ),
                P(cls=(TextFont.muted_sm, "text-center"))(
                    "By clicking continue, you agree to our ",
                    A(
                        cls="underline underline-offset-4 hover:text-primary",
                        href="#demo",
                        uk_toggle=True,
                    )("Terms of Service"),
                    " and ",
                    A(
                        cls="underline underline-offset-4 hover:text-primary",
                        href="#demo",
                        uk_toggle=True,
                    )("Privacy Policy"),
                    ".",
                ),
            )
        ),
    )

    return Grid(left, right, cols=2, gap=0, cls="h-screen")


@rt("/auth/register")
async def post(request):
    try:
        form = await request.form()
        email = form.get("email")
        password = form.get("password")

        if not email or not password:
            add_custom_toast(
                request.session, f"Wrong credentials for: {email}", "error"
            )
            return RedirectResponse(url="#", status_code=303)

        user = await auth_service.register(request, password, email)
        if user:
            request.session["user"] = user.model_dump_json(
                include={"email": True, "id": True}
            )
            return RedirectResponse(url="/dashboard", status_code=303)
        add_custom_toast(request.session, f"Registration faild: {email}", "error")
        return RedirectResponse(url="#", status_code=303)
    except Exception as e:
        add_custom_toast(request.session, f"Registration faild: {e}", "error")
        return RedirectResponse(url="#", status_code=303)