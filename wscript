# -*- Mode: python; py-indent-offset: 4; indent-tabs-mode: nil; coding: utf-8; -*-

# def options(opt):
#     pass

# def configure(conf):
#     conf.check_nonfatal(header_name='stdint.h', define_name='HAVE_STDINT_H')

def build(bld):
    module = bld.create_ns3_module('cognitive', ['core', 'network'])
    module.source = [
        'model/repository.cc',
        'model/pu-model.cc',
        'model/spectrum-data.cc',
        'model/spectrum-manager.cc',
        'model/spectrum-decision.cc',
        'model/spectrum-sensing.cc',
        'model/cognitive-packet-tags.cc',
#        'helper/cognitive-helper.cc',
        ]

    module_test = bld.create_ns3_module_test_library('cognitive')
    module_test.source = [
        'test/cognitive-test-suite.cc',
        ]

    headers = bld(features='ns3header')
    headers.module = 'cognitive'
    headers.source = [
        'model/repository.h',
        'model/pu-model.h',
        'model/spectrum-data.h',
        'model/spectrum-manager.h',
        'model/spectrum-decision.h',
        'model/spectrum-sensing.h',
        'model/common-cognitive-header.h',
        'model/cognitive-packet-tags.h',
#        'helper/cognitive-helper.h',
        ]

    if bld.env.ENABLE_EXAMPLES:
        bld.recurse('examples')

    # bld.ns3_python_bindings()

