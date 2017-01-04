#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Diego Linayo'
import csv
import time


class Singleton(type):
  _instances = {}
  def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]



class LectoPelis():

    __metaclass__ = Singleton

    @staticmethod
    def parsear_csv(file):
        with open(file, 'rb') as fp:
            listado = csv.DictReader(fp)
            for registro in listado:
                yield registro




class Procesador():

    def __init__(self, file):
        self.listado = LectoPelis().parsear_csv(file)
        self.reporte = Reporte()


    def calcular(self):
        duplicados = set()
        for registro in self.listado:
            if registro['movie_title'] in duplicados:
                continue
            duplicados.add(registro['movie_title'])
            self.reporte.update(registro)


        print (repr(self.reporte))


class ClassBasedDecorator(object):

    def __init__(cls, func_to_decorate):
        cls.func_to_decorate = func_to_decorate

    def __call__(cls, *args, **kwargs):
        return cls.func_to_decorate(object)


class calcularData:

  def __init__(self):
      pass

  def __call__(self,function):
    def wrapper(self,*args,**kwargs):
        data,slice_i,slice_e =  function(self)
        return sorted(data.iteritems(), key=lambda (k,v): (v,k))[slice_i:slice_e]
    return wrapper


class Reporte():
    __metaclass__ = Singleton

    contador_color = 0
    contador_bn = 0
    contador_vacio = 0
    directores = {}
    criticas = {}
    duracion = {}
    recaudacion = {}
    presupuesto = {}
    producciones_anuales = {}

    def update(self, registro):
        self.update_contador_color(registro)
        self.update_directores(registro)
        self.update_menos_criticas(registro)
        self.update_duracion(registro)
        self.update_recaudacion(registro)
        self.update_presupuesto(registro)
        self.update_producciones_anuales(registro)

    def update_contador_color(self, registro):
        if registro['color'] == 'Color':
            self.contador_color += 1
        elif registro['color'] == ' Black and White':
            self.contador_bn += 1
        else:
            self.contador_vacio += 1


    def update_directores(self, registro):
        key = unicode(registro['director_name'] , 'utf-8')
        if(key != ''):
            if (self.directores.has_key(key)):
                self.directores[key]['total'] +=1
                self.directores[key]['imdb_score'] += float(registro['imdb_score'])
            else:
                self.directores[key] = {}
                self.directores[key]['total'] = 1
                self.directores[key]['imdb_score'] = float(registro['imdb_score'])


    def update_menos_criticas(self, registro ):
        if registro['movie_title'] != '' and registro['num_critic_for_reviews'] != '':
            self.criticas[registro['movie_title'].replace('\xc2\xa0', '')] = registro['num_critic_for_reviews']

    @calcularData()
    def get_criticas(self):
        return self.criticas,None, 10


    def update_duracion(self, registro):
        if registro['movie_title'] != '' and registro['duration'] > 0 and registro['duration'] != '':
            self.duracion[registro['movie_title'].replace('\xc2\xa0', '').strip()] = int(registro['duration'])

    @calcularData()
    def get_mayor_duracion(self):
        return self.duracion, -20, None

    def update_recaudacion(self, registro):
        if registro['movie_title'] != '' and registro['gross'] > 0 and registro['gross'] != '':
            self.recaudacion[registro['movie_title'].replace('\xc2\xa0', '').strip()] = int(registro['gross'])

    @calcularData()
    def get_mayor_recaudacion(self):
        return self.recaudacion, -5, None

    @calcularData()
    def get_menor_recaudacion(self):
        return self.recaudacion , None, 5



    def update_presupuesto(self, registro):
        if registro['movie_title'] != '' and registro['budget'] > 0 and registro['budget'] != '':
            self.presupuesto[registro['movie_title'].replace('\xc2\xa0', '').strip()] = int(registro['budget'])


    @calcularData()
    def get_mayor_presupuesto(self):
        return self.presupuesto, -3, None

    @calcularData()
    def get_menor_presupuesto(self):
        return self.presupuesto, None, 3

    def update_producciones_anuales(self, registro):
        if(registro['title_year'] != ''):

            key = int(registro['title_year'])
            if key != '' and key > 0 :
                if (self.producciones_anuales.has_key(key)):
                    self.producciones_anuales[key] += 1
                else:
                     self.producciones_anuales[key] = 1

    @calcularData()
    def get_menor_producciones_anuales(self):
        return self.producciones_anuales, None, 1

    @calcularData()
    def get_mayor_producciones_anuales(self):
        return  self.producciones_anuales, -1, None

    @calcularData()
    def get_director_mejor_reuputacion(self):
        tmp = {}
        for director_item in self.directores:
            tmp[director_item] = self.directores[director_item]['imdb_score']/ self.directores[director_item]['total']

        return tmp,-5, None


    def __repr__(self):
        #for item in self.directores:
        #    print "Director: %s Cantidad Producciones: %s" % (item, self.directores[item]['total'])

        # print self.get_director_mejor_reuputacion()
        #print [[director_item] for director_item in ]

        # print self.get_criticas()
        # print self.get_mayor_duracion()
        #
        # print self.get_mayor_recaudacion()
        # print self.get_menor_recaudacion()
        #
        # print self.get_mayor_presupuesto()
        # print self.get_menor_presupuesto()
        #
        # print self.get_menor_producciones_anuales()
        # print self.get_mayor_producciones_anuales()

        return str(vars(self))



if __name__ == '__main__':
    start_time = time.time()
    procesador = Procesador('resources/movie_metadata.csv')
    procesador.calcular()
    print ('Benchmark {0:.3f} Segundos'.format(time.time() - start_time))




