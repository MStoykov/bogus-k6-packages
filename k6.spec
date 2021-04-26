Name: k6
Version: 0.31.1
Release: 2.changerepo
License: LICENSE
Url: https://k6.io/
Summary: Load testing for the 21st century

%description
k6 is a developer centric open source load testing tool for testing the performance of your backend infrastructure. It’s built with Go and JavaScript to integrate well into your development workflow, so you can stay on top of performance without fuzz.

%pre -p /bin/sh

echo -e "\e[32mThe repo you are using for installing k6 is being shutdown as a result of Bintray sunsetting its service on May 1st 2021.\e[0m
The k6 team has made available a new repository where future packages will be published.
In order to upgrade we recommend that you follow the new installation instructions at https://k6.io/docs/getting-started/installation/ and remove the Bintray repository and key as mentioned in the \"Note about Bintray\" section."
exit 1

%install

%files

%changelog
* Thu Apr 22 2021 Load Impact
 - package to mention we need to move
