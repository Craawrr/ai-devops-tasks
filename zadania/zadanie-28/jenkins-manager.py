
#!/usr/bin/env python3

import os
import sys
import requests
from requests.auth import HTTPBasicAuth
from requests.exceptions import RequestException

class JenkinsManager:
    def __init__(self):
        self.url = os.getenv("JENKINS_URL", "").rstrip("/")
        self.username = os.getenv("JENKINS_USER")
        self.token = os.getenv("JENKINS_TOKEN")

        if not self.url or not self.username or not self.token:
            raise ValueError(
                "Ustaw zmienne JENKINS_URL, JENKINS_USER i JENKINS_TOKEN"
            )

        self.session = requests.Session()
        self.session.auth = HTTPBasicAuth(self.username, self.token)
        self.session.headers.update({
            "Accept": "application/json"
        })

        self.timeout = 15

    def request(self, method, endpoint, **kwargs):
        url = f"{self.url}/{endpoint.lstrip('/')}"

        try:
            response = self.session.request(
                method, url, timeout=self.timeout, **kwargs
            )
            response.raise_for_status()
            return response

        except requests.exceptions.HTTPError as e:
            print(f"Błąd HTTP: {e}", file=sys.stderr)
        except requests.exceptions.ConnectionError:
            print("Nie można połączyć się z Jenkins.", file=sys.stderr)
        except requests.exceptions.Timeout:
            print("Przekroczono limit czasu połączenia.", file=sys.stderr)
        except RequestException as e:
            print(f"Błąd komunikacji: {e}", file=sys.stderr)

        return None

    def list_jobs(self):
        response = self.request(
            "GET", "/api/json",
            params={"tree": "jobs[name,color,url]"}
        )

        if response is None:
            return

        jobs = response.json().get("jobs", [])

        print("\nLista zadań Jenkins:")
        for job in jobs:
            print(
                f"- {job['name']} | Status: {job['color']} "
                f"| URL: {job['url']}"
            )

    def check_build_status(self, job_name):
        endpoint = f"/job/{job_name}/lastBuild/api/json"

        response = self.request(
            "GET", endpoint,
            params={"tree": "number,result,building,timestamp,url"}
        )

        if response is None:
            return

        build = response.json()

        print(f"\nZadanie: {job_name}")
        print(f"Build: {build.get('number')}")
        print(f"Wynik: {build.get('result') or 'W trakcie'}")
        print(f"Czy trwa: {build.get('building')}")
        print(f"URL: {build.get('url')}")

    def run_job(self, job_name):
        endpoint = f"/job/{job_name}/build"

        response = self.request("POST", endpoint)

        if response is None:
            return

        if response.status_code in (200, 201, 202):
            print(f"Zadanie '{job_name}' zostało uruchomione.")
        else:
            print(f"Nie udało się uruchomić zadania: {response.status_code}")


def main():
    try:
        jenkins = JenkinsManager()

        if len(sys.argv) < 2:
            print("Użycie:")
            print("  python jenkins-manager.py list")
            print("  python jenkins-manager.py status NAZWA_ZADANIA")
            print("  python jenkins-manager.py run NAZWA_ZADANIA")
            return

        command = sys.argv[1]

        if command == "list":
            jenkins.list_jobs()

        elif command == "status" and len(sys.argv) == 3:
            jenkins.check_build_status(sys.argv[2])

        elif command == "run" and len(sys.argv) == 3:
            jenkins.run_job(sys.argv[2])

        else:
            print("Nieznane polecenie lub nieprawidłowe argumenty.")

    except ValueError as e:
        print(f"Błąd konfiguracji: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
