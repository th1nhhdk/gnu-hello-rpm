# gnu-hello-rpm
## My first rpm (Fedora 35) package :D

## How to build
### https://docs.fedoraproject.org/en-US/package-maintainers/Installing_Packager_Tools/
`fedpkg --release f35 mockbuild`

## How to check spec file (Build first!!!)
`rpmlint hello.spec ./results_hello/2.12/1.fc35/hello-2.12-*.{x86_64,src}.rpm`
