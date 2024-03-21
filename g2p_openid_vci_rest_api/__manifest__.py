{
    "name": "G2P OpenID VCI: Rest API",
    "category": "G2P",
    "version": "15.0.1.2.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "MPL-2",
    "development_status": "Alpha",
    "depends": [
        "g2p_openid_vci",
        "component",
        "pydantic",
        "base_rest",
        "base_rest_pydantic",
        "extendable",
    ],
    "external_dependencies": {
        "python": ["extendable-pydantic", "pydantic==1.10.10", "pyjq"]
    },
    "data": [],
    "assets": {
        "web.assets_backend": [],
        "web.assets_qweb": [],
    },
    "demo": [],
    "images": [],
    "application": False,
    "installable": True,
    "auto_install": False,
}
