# gnu-hello-spec
## rpm spec package template (Fedora Linux 36)

## How to build
```
# dnf install fedora-packager fedora-review
# usermod -a -G mock <your username>
$ cd ..
$ mv gnu-hello-spec hello
$ cd hello
$ fedpkg --release f36 mockbuild
```

## How to check spec file
`rpmlint hello.spec`

(or after build)
`rpmlint hello.spec results_hello/2.12.1/1.fc36/hello-2.12.1*.rpm`
