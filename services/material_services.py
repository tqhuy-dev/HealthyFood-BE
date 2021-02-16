import model
import repository


def add_material(pg_db, request):
    data = request.json
    material = model.MaterialModel(0,
                                   data["name"],
                                   data["status"],
                                   data["quantity"],
                                   data["unit"],
                                   data["description"],
                                   data["material_type"],
                                   ",".join(data["image"]))

    try:
        material_repo = repository.MaterialRepository(pg_db)
        material_repo.add_material(material)
    except:
        return False, "Internal Error:Execute Error"
    return True, "Success"
