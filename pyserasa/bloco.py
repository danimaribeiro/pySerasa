# -*- coding: utf-8 -*-


class Bloco(object):

    def __getitem__(self, key):
        campo = ([c for c in self.campos if c.indice == key or c.nome == key] or [None])[0]
        if not campo:
            raise 'Este campo ' + key + ' não existe neste bloco de registros'
        return campo.get(self)

    def __getattr__(self, name):
        campo = ([c for c in self.campos.campos if c._nome == name] or [None])[0]
        if not campo:
            raise 'Este campo ' + name + ' não existe neste bloco de registros'
        else:
            return campo._valor
