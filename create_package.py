import dtlpy as dl
import logging

logger = logging.getLogger(name=__name__)

project = dl.projects.get(project_id='project_id')

# build the module for the package
module = dl.PackageModule(entry_point='main.py',
                          class_name='ServiceRunner',
                          functions=[
                              dl.PackageFunction(name='run',
                                                 inputs=[dl.FunctionIO(type="Item", name="item")]
                                                 , description='')
                          ])

package = project.packages.push(package_name='package-git',
                                modules=[module],
                                codebase=dl.GitCodebase(
                                    git_url='https://github.com/dataloop-ai/package_git_example.git',
                                    git_tag='main'))

# deploy the service for the first time
service = package.services.deploy(package=package,
                                  runtime={"gpu": False, "numReplicas": 1, 'concurrency': 1,
                                           'autoscaler': {
                                               'type': dl.KubernetesAutuscalerType.RABBITMQ,
                                               'minReplicas': 1,
                                               'maxReplicas': 5,
                                               'queueLength': 10}}
                                  )

# to update the service
service = package.services.get(service_name=package.name)
service.package_revision = package.version
service.update()
