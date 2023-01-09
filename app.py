#!/usr/bin/env python3

import aws_cdk as cdk

from cdk_proj_1.cdk_proj_1_stack import CdkProj1Stack


app = cdk.App()
CdkProj1Stack(app, "cdk-proj-1")

app.synth()
