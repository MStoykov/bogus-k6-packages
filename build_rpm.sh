#!/bin/bash
rpmbuild -bb   --define "_topdir $PWD/RPMBUILD" k6.spec
