import json
from textwrap import indent


class MfeCli:

    configs: str = {}

    def read_config(self, config_file: str = 'mfe.config.json'):
        f = open(config_file)
        self.configs = json.load(f)
        f.close()

    def generate(self):
        for appName, app in self.configs['apps'].items():
            print(appName, '->', app)

            # Overwrite angular.json file by angular.mfe.json
            self._generate_angular_json(appName, app)

            # Add webpack.config.json file
            self._generate_webpack_js(appName, app)

            # Sample
            self._generate_sample(appName, app)

    def _generate_angular_json(self, appName: str, app: dict):
        angular_json_template_path = f'.templates/angular.mfe.json'
        angular_json_path = f'{appName}/angular.json'
        angular_json_template = None 
        port = app['port'] if 'port' in app else 4200

        with open(angular_json_template_path) as f:
            angular_json_template_str = json.dumps(json.load(f))

            # Replace appName
            angular_json_template_str = angular_json_template_str.replace('__mfe_appName__', appName)

            # Replace app port
            angular_json_template_str = angular_json_template_str.replace('4200', str(port))

            # Parse to JSON format again
            angular_json_template = json.loads(angular_json_template_str)
            
            # Writi final angular.json file
            with open(angular_json_path, 'w') as f:
                json.dump(angular_json_template, f, indent=2)

    def _generate_webpack_js(self, appName: str, app: dict):
        
        if appName == 'layout':
            appType = 'layout'
        elif appName == 'shell':
            appType = 'layout'
        else:
            appType = 'app' 

        # Write webpack.config.js
        webpack_json_template_path = f'.templates/webpack.config.{appType}.js'
        webpack_json_path = f'{appName}/webpack.config.js'
        port = app['port'] if 'port' in app else 4200

        print(webpack_json_template_path)

        with open(webpack_json_template_path) as f:
            webpack_json_template_str = f.read()

            # Replace appName
            webpack_json_template_str = webpack_json_template_str.replace('__mfe_appName__', appName)

            # Replace appName
            webpack_json_template_str = webpack_json_template_str.replace('__mfe_appModuleName__', f"{appName.title()}Module")

            # Replace app port
            webpack_json_template_str = webpack_json_template_str.replace('4200', str(port))

            # Writi final webpack.json file
            with open(webpack_json_path, 'w') as f:
                f.write(webpack_json_template_str)

        # Write webpack.config.prod.js
        webpack_json_prod_template_path = f'.templates/webpack.prod.config.{appType}.js'
        webpack_json_prod_path = f'{appName}/webpack.prod.config.js'

        with open(webpack_json_prod_template_path) as f:
            webpack_json_prod_template_str = f.read()
            
            with open(webpack_json_prod_path, 'w') as f:
                f.write(webpack_json_prod_template_str)

    def _generate_sample(self, appName: str, app: dict):
        angular_app_file = f'{appName}/src/app/app.component.html'
        with open(angular_app_file, 'w') as f:
            f.write(f'<h3>{appName} works!</h3>')
            f.write(f"\n<router-outlet></router-outlet>")

        # Copy shell app
        import shutil
        shutil.copytree('.templates/shell', 'shell', dirs_exist_ok=True)

            
if __name__ == "__main__":
    mfecli = MfeCli()

    # Read configuration
    mfecli.read_config()
    print(mfecli.configs)

    # Generate apps
    mfecli.generate()