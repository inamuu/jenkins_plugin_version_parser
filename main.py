# coding: utf-8

import re
import requests
import time
from bs4 import BeautifulSoup

def create_list():
    with open('files/list.txt', 'r', encoding="utf-8") as f:
        list = f.readlines()
    return list

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
                plugin_version = i.text.replace('Version', '').replace(' ', '').replace(':', '')
            if re.match('Requires Jenkins', i.text):
                jenkins_version = i.text.replace('Requires Jenkins', '').replace(' ', '')
        print(plugin_name + ", " + plugin_version + ", " + jenkins_version)
        time.sleep(0.5)

def main():
    list = create_list()
    parse_jenkins_plugin(list)


if __name__ == '__main__': main()

