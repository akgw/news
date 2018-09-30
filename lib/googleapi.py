from __future__ import print_function
import os
import argparse
import httplib2
from googleapiclient.discovery import build
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
from constants import constants


class GoogleAPI:

    SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
    CLIENT_SECRET_FILE = 'client_secret.json'
    APPLICATION_NAME = 'Google Sheets API Python Quickstart'
    SPREAD_SHEET_ID = '1LQ74GYE4lG5ZGcFv4sbrP1wHvidcksmulXW8H-PlLGw'

    def __init__(self):
        try:
            self.flags = argparse.ArgumentParser(
                parents=[tools.argparser]).parse_args()
        except ImportError:
            self.flags = None

        credentials = self.get_credentials()

        http = credentials.authorize(httplib2.Http())
        discovery_url = ('https://sheets.googleapis.com/$discovery/rest?'
                         'version=v4')
        self.service = build('sheets', 'v4', http=http,
                                       discoveryServiceUrl=discovery_url)

    def get_credentials(self):
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(
            credential_dir, 'sheets.googleapis.com-python-quickstart.json')

        store = Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets(
                self.CLIENT_SECRET_FILE, self.SCOPES)
            flow.user_agent = self.APPLICATION_NAME
            if self.flags:
                credentials = tools.run_flow(flow, store, self.flags)
            else:
                credentials = tools.run(flow, store)
            print('Storing credentials to ' + credential_path)
        return credentials

    def get_values(self, sheet_name):
        sheet = constants.sheet_dic[sheet_name]

        request = self.service.spreadsheets().values().get(
            spreadsheetId=self.SPREAD_SHEET_ID, range=sheet_name + '!' + sheet['range'])
        values = request.execute().get('values', [])

        values.pop(0)
        ret_value = []
        for column_index, value in enumerate(values):
            if len(value) != len(sheet['map']):
                print(str(value) + 'is not enough value')
                continue

            v = {}
            for index, key in sheet['map'].items():
                v[key] = value[index]

            v['column_index'] = column_index + 2  # popしているため2から開始
            ret_value.append(v)

        return ret_value

    def set_values(self, sheet_name, text_list):
        sheet = constants.sheet_dic[sheet_name]

        for value in text_list.values():
            target = sheet_name + '!' + \
                sheet['output_range'] + str(value['column_index'])

            body = {
                'values': [
                    [
                        str(sorted(value['point'].items(),
                                   key=lambda x: -x[1]))
                    ],
                ]
            }

            self.service.spreadsheets().values().update(
                spreadsheetId=self.SPREAD_SHEET_ID, valueInputOption='RAW', range=target, body=body).execute()
