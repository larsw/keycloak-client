#! -*- coding: utf-8 -*-

""" custom exceptions for keycloak client """


class InvalidAuthorizationCode(Exception):
    """ Exception for wrong AuthorizationCode """


class InvalidAAT(Exception):
    """ Exception for wrong AAT """


class InvalidPermissionTicket(Exception):
    """ Exception for wrong permission ticket """


class InvalidRPT(Exception):
    """ Exception for wrong RPT """


class InvalidPolicy(Exception):
    """ Exception for wrong policy """


class InvalidResource(Exception):
    """ Exception for wrong policy """


class InvalidPermission(Exception):
    """ Exception for wrong permission """
