"""FrankenUI Dashboard Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../example_dashboard.ipynb.

# %% auto 0
__all__ = [
    "rev",
    "sub",
    "sal",
    "act",
    "top_info_row",
    "recent_sales",
    "teams",
    "opt_hdrs",
    "team_dropdown",
    "hotkeys",
    "avatar_dropdown",
    "top_nav",
    "dashboard_homepage",
    "InfoCard",
    "AvatarItem",
    "generate_chart",
    "NavSpacedLi",
    "page",
]

# %% ../example_dashboard.ipynb
from fasthtml.common import *
from fh_frankenui import *
from fh_frankenui.core import *

from fasthtml.svg import *
from fasthtml.core import APIRouter
from ..templates import app_template


# %% ../example_dashboard.ipynb
def InfoCard(title, value, change):
    return Div(Card(Div(H3(value), P(change, cls=TextFont.muted_sm)), header=H4(title)))


# %% ../example_dashboard.ipynb
rev = InfoCard("Total Revenue", "$45,231.89", "+20.1% from last month")
sub = InfoCard("Subscriptions", "+2350", "+180.1% from last month")
sal = InfoCard("Sales", "+12,234", "+19% from last month")
act = InfoCard("Active Now", "+573", "+201 since last hour")

# %% ../example_dashboard.ipynb
top_info_row = Grid(rev, sub, sal, act, cols=4)


# %% ../example_dashboard.ipynb
def AvatarItem(name, email, amount):
    return Div(cls="flex items-center")(
        DiceBearAvatar(name, 9, 9),
        Div(cls="ml-4 space-y-1")(
            P(name, cls=TextFont.bold_sm), P(email, cls=TextFont.muted_sm)
        ),
        Div(amount, cls="ml-auto font-medium"),
    )


recent_sales = Card(
    Div(cls="space-y-8")(
        *[
            AvatarItem(n, e, d)
            for (n, e, d) in (
                ("Olivia Martin", "olivia.martin@email.com", "+$1,999.00"),
                ("Jackson Lee", "jackson.lee@email.com", "+$39.00"),
                ("Isabella Nguyen", "isabella.nguyen@email.com", "+$299.00"),
                ("William Kim", "will@email.com", "+$99.00"),
                ("Sofia Davis", "sofia.davis@email.com", "+$39.00"),
            )
        ]
    ),
    header=Div(
        H3("Recent Sales"), P("You made 265 sales this month.", cls=TextFont.muted_sm)
    ),
    cls="col-span-3",
)


# %% ../example_dashboard.ipynb
teams = [["Alicia Koch"], ["supa_app", "Monster Inc."], ["Create a Team"]]

opt_hdrs = ["Personal", "Team", ""]

team_dropdown = UkSelect(
    Optgroup(label="Personal Account")(Option(A("Alicia Koch"))),
    Optgroup(label="Teams")(Option(A("supa_app")), Option(A("Monster Inc."))),
    Option(A("Create a Team")),
)

rt = APIRouter()


@rt("/dashboard")
@app_template("Dashboard")
def page(request):
    return Div(cls="space-y-4")(
        H2("Dashboard"),
        TabContainer(
            Li(A("Overview", cls="uk-active")),
            Li(A("Analytics")),
            Li(A("Reports")),
            Li(A("Notifications")),
            uk_switcher="connect: #component-nav; animation: uk-animation-fade",
            alt=True,
        ),
        Ul(id="component-nav", cls="uk-switcher")(
            Li(
                top_info_row,
                Grid(
                    Card(H3("Overview to show here..."), cls="col-span-4"),
                    recent_sales,
                    gap=4,
                    cols=7,
                ),
                cls="space-y-4",
            ),
            Li(
                top_info_row,
                Grid(
                    Card(H3("Analytics to show here..."), cls="col-span-4"),
                    recent_sales,
                    gap=4,
                    cols=7,
                ),
                cls="space-y-4",
            ),
        ),
    )
