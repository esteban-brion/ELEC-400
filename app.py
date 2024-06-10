
import firebase_admin
from firebase_admin import credentials, firestore

# Initialiser Firebase
cred = credentials.Certificate('/Users/esteban/Desktop/key.json')
firebase_admin.initialize_app(cred)

# Initialiser Firestore
db = firestore.client()

def add_document(data):
    try:
        doc_ref = db.collection('your_collection').add(data)
        print(f"Document ajouté avec ID : {doc_ref[1].id}")
    except Exception as e:
        print(f"Erreur d'ajout du document : {e}")

def get_document(doc_id):
    try:
        doc_ref = db.collection('your_collection').document(doc_id)
        doc = doc_ref.get()
        if doc.exists:
            print(f"Données du document : {doc.to_dict()}")
        else:
            print("Aucun document trouvé !")
    except Exception as e:
        print(f"Erreur de récupération du document : {e}")

def update_document(doc_id, data):
    try:
        doc_ref = db.collection('your_collection').document(doc_id)
        doc_ref.update(data)
        print("Document mis à jour avec succès")
    except Exception as e:
        print(f"Erreur de mise à jour du document : {e}")

def delete_document(doc_id):
    try:
        doc_ref = db.collection('your_collection').document(doc_id)
        doc_ref.delete()
        print("Document supprimé avec succès")
    except Exception as e:
        print(f"Erreur de suppression du document : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    # Ajouter un document
    add_document({"field1": "value1", "field2": "value2"})

    # Récupérer un document
    get_document("your_document_id")

    # Mettre à jour un document
    update_document("your_document_id", {"field1": "new_value"})

    # Supprimer un document
    delete_document("your_document_id")
