from fasthtml.common import *


def ctas():
    return Section(
        Div(
            Div(
                H2(
                    "Let's find more that brings us together.",
                    cls="mb-4 text-4xl tracking-tight font-extrabold text-gray-900 dark:text-white",
                ),
                P(
                    "super_app helps you connect with friends, family and communities of people who share your interests. Connecting with your friends and family as well as discovering new ones is easy with features like Groups, Watch and Marketplace.",
                    cls="mb-8 font-light text-gray-500 sm:text-xl dark:text-gray-400",
                ),
                Div(
                    A(
                        "Get started",
                        href="#",
                        cls="inline-flex items-center justify-center px-4 py-2.5 text-base font-medium text-center text-white bg-primary-700 rounded-lg hover:bg-primary-800 focus:ring-4 focus:ring-primary-300 dark:focus:ring-primary-900",
                    ),
                    A(
                        Svg(
                            Path(
                                d="M2 6a2 2 0 012-2h6a2 2 0 012 2v8a2 2 0 01-2 2H4a2 2 0 01-2-2V6zM14.553 7.106A1 1 0 0014 8v4a1 1 0 00.553.894l2 1A1 1 0 0018 13V7a1 1 0 00-1.447-.894l-2 1z"
                            ),
                            fill="currentColor",
                            viewbox="0 0 20 20",
                            xmlns="http://www.w3.org/2000/svg",
                            cls="mr-2 -ml-1 w-5 h-5",
                        ),
                        "View more",
                        href="#",
                        cls="inline-flex items-center justify-center px-4 py-2.5 text-base font-medium text-center text-gray-900 border border-gray-300 rounded-lg hover:bg-gray-100 focus:ring-4 focus:ring-gray-100 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:focus:ring-gray-600",
                    ),
                    cls="flex flex-col space-y-4 sm:flex-row sm:space-y-0 sm:space-x-4",
                ),
                cls="max-w-screen-md",
            ),
            cls="py-8 px-4 mx-auto max-w-screen-xl sm:py-16 lg:px-6",
        ),
        cls="bg-white dark:bg-gray-900",
    )
