from sktime.utils import all_estimators
from importlib import import_module

estimators = all_estimators(estimator_types="classifier")
for modname, modclass in estimators:
    try:
        print(modname, modclass.__author__)
    except AttributeError:
        try:
            print(modname, import_module(modclass.__module__).__author__)
        except AttributeError:
            print(modname, "no author info")
