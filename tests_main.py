from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main_returns_not_found():
    response = client.get('/')
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}

def test_read_items_returns_list():
    response_alpha = client.post('/task', 
    json={
  "description": "Buy baby diapers",
  "completed": False
    }
    )
    assert response_alpha.status_code == 200

    response_beta = client.post('/task', 
    json={
  "description": "Buy milk bag",
  "completed": False
    }
    )
    assert response_beta.status_code == 200

    response_get_all = client.get('/task')
    assert response_get_all.status_code == 200
    assert response_get_all.json()=={
        response_alpha.json(): {
            "description": "Buy baby diapers",
            "completed": False
        },
        response_beta.json(): {
            "description": "Buy milk bag",
            "completed": False
        }
    }
    response_delete_alpha = client.delete(f"/task/{response_alpha.json()}")
    assert response_delete_alpha.status_code == 200

    response_delete_beta = client.delete(f"/task/{response_beta.json()}")
    assert response_delete_beta.status_code == 200

def test_post_items_returns_success():
    response_alpha = client.post('/task', 
    json={
  "description": "Buy baby diapers",
  "completed": False
    }
    )
    assert response_alpha.status_code == 200

def test_read_item_returns_item():
    response_alpha = client.post('/task', 
    json={
  "description": "Buy baby diapers",
  "completed": False
    }
    )
    assert response_alpha.status_code == 200

   
    response_get = client.get(f"/task/{response_alpha.json()}")

    assert response_get.status_code == 200
    assert response_get.json()=={
            "description": "Buy baby diapers",
            "completed": False
        }
    
    response_delete_alpha = client.delete(f"/task/{response_alpha.json()}")
    assert response_delete_alpha.status_code == 200

def test_put_item_returns_item():
    response_alpha = client.post('/task', 
    json={
  "description": "Buy baby diapers",
  "completed": False
    }
    )
    assert response_alpha.status_code == 200

    
    response_put = client.put(f"/task/{response_alpha.json()}",json={
        "description": "Buy milk bag",
        "completed": False
        }
        )

    assert response_put.status_code == 200

    response_get = client.get(f"/task/{response_alpha.json()}")

    assert response_get.status_code == 200
    assert response_get.json()=={
            "description": "Buy milk bag",
            "completed": False
    }
    
    response_delete_alpha = client.delete(f"/task/{response_alpha.json()}")
    assert response_delete_alpha.status_code == 200

def test_delete_item_returns_success():
    response_alpha = client.post('/task', 
    json={
  "description": "Buy baby diapers",
  "completed": False
    }
    )
    assert response_alpha.status_code == 200

    response_delete_alpha = client.delete(f"/task/{response_alpha.json()}")
    assert response_delete_alpha.status_code == 200

def test_patch_item_returns_item():
    response_alpha = client.post('/task', 
    json={
  "description": "Buy baby diapers",
  "completed": False
    }
    )
    assert response_alpha.status_code == 200

    
    response_patch = client.patch(f"/task/{response_alpha.json()}",json={
        "description": "Buy baby diapers",
        "completed": True
        }
        )

    assert response_patch.status_code == 200

    response_get = client.get(f"/task/{response_alpha.json()}")

    assert response_get.status_code == 200
    assert response_get.json()=={
        "description": "Buy baby diapers",
        "completed": True
        }
    
    response_delete_alpha = client.delete(f"/task/{response_alpha.json()}")
    assert response_delete_alpha.status_code == 200  