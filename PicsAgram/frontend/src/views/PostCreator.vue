<template>
<div class="post-creator">
    <div class="container">
        <div class="row mt-3">
            <div class="col-12">
                <h2 class="text-center mb-5">Crea un nuovo Post</h2>
                <form enctype="multipart/form-data" @submit.prevent="addPost">
                    <input
                        type="file"
                        id="image"
                        class="form-control-file mt-2"
                        required
                        @change="onImageSelected">
                    <textarea
                        v-model="description"
                        class="form-control my-2"
                        rows="3"
                        placeholder="Inserisci una descrizione..."
                    ></textarea>
                    <button 
                        type="submit"
                        class="btn btn-sm btn-success"
                    >Aggiungi Post</button>
                </form>
                <p class="error mt-2">{{ error }}</p>
            </div>
        </div>
    </div>
</div>
</template>

<script>
// npm install --save axios
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "PostCreator",
    data() {
        return {
            description: null,
            image: null,
            error: null
        }
    },
    methods: {
        onImageSelected(event) {
            this.image = event.target.files[0];
        },
        async addPost(){
            if(this.image){
                let form_data = new FormData();
                form_data.append('image', this.image);
                if(this.description){form_data.append('description', this.description);}
                await axios.post('http://localhost:8000/api/posts/',
                                  form_data,
                                  {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                        "X-CSRFToken": CSRF_TOKEN
                                    }
                                })
                        .then( () => {
                            this.$router.push('/');
                        })
            }else {
                this.error = "Devi inserire un'immagine!";
            }
        }
    },
    created() {
        document.title = "PicsAgram - Post Editor";
    }
}
</script>

<style>
.error{
    color: red;
    font-weight: bold;
}
</style>