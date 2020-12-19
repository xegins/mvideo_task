from server import run_server


def read_config():
    server_params = {}
    with open("config.cfg") as config_file:
        for row in config_file:
            splited_row = row.strip().split("=")
            if len(splited_row) == 2:
                server_params[splited_row[0]] = splited_row[1]
    return server_params


if __name__ == '__main__':
    run_server(**read_config())
