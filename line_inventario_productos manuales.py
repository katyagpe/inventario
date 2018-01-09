#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import csv
import xmlrpclib
import re


HOST='localhost'
PORT=8069
DB='4toAngulo_pruebas'
USER='salas-rodriguez@hotmail.com'
PASS='agosto1993'
url ='http://%s:%d/xmlrpc/' % (HOST,PORT)

common_proxy = xmlrpclib.ServerProxy(url+'common')
object_proxy = xmlrpclib.ServerProxy(url+'object')
uid = common_proxy.login(DB,USER,PASS)


def _create(estado):
    if estado is True:
        path_file = './line_inventario_productos manuales.csv'
        archive = csv.DictReader(open(path_file))
        cont = 1

        for field in archive:
            print field

            
            vals = {
                'inventory_id':field['inventory_id'],
                'product_qty':field['product_qty'],
                'create_uid':field['create_uid'],
                'product_id':field['product_id'],
                'location_id':field['location_id'],
                'product_uom_id':field['product_uom_id'],
                'package_id':field['package_id'],
            }

            do_write = object_proxy.execute(DB,uid,PASS,'stock.inventory.line','create',vals)
            if do_write:
                cont = cont + 1
                print "Contador:",cont
            else:
                print "Error"

def __main__():
    print 'Ha comenzado el proceso'
    _create(True)
    print 'Ha finalizado la carga tabla'
__main__()