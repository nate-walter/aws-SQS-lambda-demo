#!/usr/bin/env python3

import aws_cdk as cdk

from sqslambdademo.sqslambdademo_stack import SqslambdademoStack


app = cdk.App()
SqslambdademoStack(app, "sqslambdademo")

app.synth()
