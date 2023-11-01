# coding: utf-8

import re
import requests
import time
from bs4 import BeautifulSoup

def create_list():
    with open('files/list.txt', 'r', encoding="utf-8") as f:
        list = f.readlines()
    return list

def replace_text(before_text):
    replace_name = before_text
    replaced_name = re.sub(':| |Version|Requires Jenkins', '', replace_name)
    return replaced_name

def parse_jenkins_plugin(list: list):
    plugin_list = list
    for plugin in plugin_list:
        plugin_name = plugin.replace(' ', '').replace('\n', '')

        load_url = "https://plugins.jenkins.io/" + plugin_name + "/"
        html = requests.get(load_url)
        soup = BeautifulSoup(html.content, "html.parser")
        requires_version = soup.find('div', class_="col-md-3 sidebar")
        for i in requires_version:
            if re.match('Version', i.text):
                plugin_version = replace_text(i.text)
            if re.match('Requires Jenkins', i.text):
                jenkins_version = replace_text(i.text)
        alert = soup.find(class_="alert alert-warning alert-with-icon")
        if alert is None:
            deprecated_text = 'Not deprecated'
        else:
            deprecated_text = 'Deprecated'
        print(plugin_name + ", " + plugin_version + ", " + jenkins_version + ", " + deprecated_text)
        time.sleep(0.5)

def main():
    list = create_list()
    parse_jenkins_plugin(list)


if __name__ == '__main__': main()

