from templateframework.runner import run
from templateframework.template import Template
from templateframework.metadata import Metadata
import subprocess
import os

class RestTemplate(Template):

    version: str
    command: str

    def pre_hook(self, metadata: Metadata) -> Metadata:
        if 'net6.0' in metadata.inputs['framework']:
            self.version = "stackspot.rest"
            self.command = "StackSpot.Template.Rest"
        else:
            self.version = "stackspot.rest.net5"
            self.command = "StackSpot.Template.Rest.5.0"

        print(f'Installing {self.version}...')
        args = ['dotnet', 'new', '-i', self.command, '--force']
        subprocess.run(args)    

        return metadata

    def post_hook(self, metadata: Metadata):
        project_name = metadata.global_inputs['project_name']
        
        args = ['dotnet', 'new', self.version, '-n', project_name, '-p', project_name, '--skipRestore', 'true', '--force', '-o', metadata.target_path]
        
        print('Creating application...')
        subprocess.run(args)

        print('Installing dotnet-format...')
        os.chdir(f'{metadata.target_path}/')
        args2 = ['dotnet', 'new', 'tool-manifest']
        subprocess.run(args2)
        args3 = ['dotnet', 'tool', 'install', '--local', 'dotnet-format']
        subprocess.run(args3)   

        print('Application Created.')

if __name__ == '__main__':
    run(RestTemplate())