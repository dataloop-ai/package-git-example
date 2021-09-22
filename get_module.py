import dtlpy as dl


def get_module():
    """
    build the module for the package
    :return:
    """
    module = dl.PackageModule(entry_point='main.py',
                              class_name='ServiceRunner',
                              functions=[
                                  dl.PackageFunction(name='run',
                                                     inputs=[dl.FunctionIO(type="Item", name="item")]
                                                     , description='')
                              ])
    return module
