import dtlpy as dl
import logging
import get_module

logger = logging.getLogger(name=__name__)

project = dl.projects.get(project_id='project_id')
package = project.packages.push(package_name='gitRepo',
                                modules=[get_module.get_module()],
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
