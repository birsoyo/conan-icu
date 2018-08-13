#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from bincrafters import build_template_default
from cpt.tools import split_colon_env

def main():
    builder = build_template_default.get_builder(pure_c=False)

    filtered_builds = []
    for settings, options, env_vars, build_requires, reference in builder.items:
        if options['icu:shared']:
            continue
        options['icu:silent'] = False
        filtered_builds.append([settings, options, env_vars, build_requires, reference])
    builder.builds = filtered_builds

    builder.run()

if __name__ == '__main__':
    main()
