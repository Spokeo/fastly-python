__author__ = 'arthur'
import fastly
import argparse
import os
import yaml

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--action", required=True, help="valid actions are 'add' and 'delete'")
    parser.add_argument("--vcl", required=True, help="path to the VCL file to be uploaded")
    args = parser.parse_args()

    for loc in os.getcwd(), os.path.expanduser("~"), "/opt/fastly-python/config/", os.getcwd() + '/config/', os.getcwd():
        try:
            with open(os.path.join(loc,"config.yml"), 'r') as f:
                config = yaml.load(f)
            service_name = config["service_name"]
            api_key = config["api_key"]
            vcl_name = config["vcl_name"]
        except IOError:
            pass

    client = fastly.connect(api_key)
    vcl_file = open(args.vcl, 'r')
    vcl_content = vcl_file.read()
    service = client.get_service_by_name(service_name)
    versions = client.list_versions(service.id)


    def get_latest(version):
        latest_version = version.pop()
        if latest_version.locked is True or latest_version.active is True:
            print "\n[ Cloning version %d ]\n"\
                % (latest_version.number)
            latest_version = client.clone_version(service.id, latest_version.number)
        return latest_version

    def upload_vcl(content):
        if vcl_name in latest.vcls:
            client.update_vcl(service.id, latest.number, vcl_name, content=vcl_content)
        else:
            client.upload_vcl(service.id, latest.number, vcl_name, vcl_content)
        client.activate_version(service.id, latest.number)

    def delete_vcl():
        vcls = client.list_vcls(service.id, latest.number)
        for vcl in vcls:
            client.delete_vcl(service.id, latest.number, vcl.name)
        client.activate_version(service.id, latest.number)


    latest = get_latest(versions)
    if args.action is 'add':
        upload_vcl(vcl_content)
    else:
        delete_vcl()


if __name__ == "__main__":
    main()

