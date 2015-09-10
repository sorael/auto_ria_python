# -*- coding: utf-8 -*-
from selenium_fixture import app


def test_search_bmw(app):
    app.go_to_home_page()
    search_options = {"price_from":"1000", "price_to":"100000", "mark": "BMW", "model":"525",
                      "region":"Киев", "year":"1990", "year_to":"2010"}
    search_options_list = []
    from_to_price = "от %s до %s $" % (search_options["price_from"], search_options["price_to"])
    search_options_list.append(from_to_price)
    mark = "%s" % search_options["mark"]
    search_options_list.append(mark)
    model = "%s" % search_options["model"]
    search_options_list.append(model)
    from_to_year = "Год от %s до %s" % (search_options["year"], search_options["year_to"])
    search_options_list.append(from_to_year)
    search_options_list.append("Киевская")
    search_options_list.append("Только с фото")
    app.fill_fields_to_search(search_options)
    app.click_search_button()
    assert app.check_text_on_search_form() == search_options_list
    if app.count() == 10:
        print("Количество объявлений равно 10")
        app.go_to_home_page()
    else:
        print("Количество объявлений не равно 10")
        app.go_to_home_page()