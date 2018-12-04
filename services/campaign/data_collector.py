campaigns = [
    {"ref": "12345", "ind": "Pharmaceuticals", "cost": "3.67", "score":"3.768", "duration": "21", "started":"05/09/18"},
    {"ref": "12346", "ind": "Pharmaceuticals", "cost": "3.67", "score":"3.768", "duration": "7", "started":"09/10/18"},
    {"ref": "24354", "ind": "Engineering", "cost": "4.54", "score": "5.578", "duration": "21", "started":"02/09/18"},
    {"ref": "24364", "ind": "Engineering", "cost": "4.54", "score": "4.578", "duration": "21", "started":"04/09/18"},
    {"ref": "24454", "ind": "Engineering", "cost": "4.54", "score": "5.578", "duration": "21", "started":"03/10/18"},
    {"ref": "24544", "ind": "Engineering", "cost": "4.54", "score": "3.578", "duration": "21", "started":"05/10/18"},
    {"ref": "31243", "ind": "CancerSupport", "cost": "7.85", "score": "4.798", "duration": "14", "started":"09/10/18"}
]

def get_all():
    return campaigns


def find_campaign(ky, vl):
    print("LOG - find_camapign - triggered")
    found = False
    res = []
    for camp in campaigns:
        if camp[ky] == vl:
            res.append(camp)
            found = True
    if found:
        return {"status": True, "result": res}
    else:
        return {"status": True, "result": res}


def get_by_id(id_ref):
    print("LOG - get_by_id - triggered")
    result = find_campaign('ref', id_ref)
    print("result : found = {}  - campaigns {}".format(result["status"], result["result"]))
    return result["result"]


def get_by_industry(id_ref):
    print("LOG - get_by_industry - triggered")
    result = find_campaign('ind', id_ref)
    print("result : found = {}  - campaigns {}".format(result["status"], result["result"]))
    return result["result"]


# get_by_id("31243")
# get_by_industry("Engineering")
