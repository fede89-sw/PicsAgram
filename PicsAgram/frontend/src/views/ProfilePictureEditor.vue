<template>
    <div class="ProfilePictureEditor mt-3">
        <div class="container">
            <form enctype="multipart/form-data" @submit.prevent="editPicture" class="row ml-2">
                <label for="image">Seleziona un'immagine per il tuo profilo</label>
                <input
                    type="file"
                    id="image"
                    class="form-control-file mt-2 mb-3"
                    @change="onImageSelected"
                >
                <button
                    type="submit"
                    class="btn btn-success"
                >Carica Foto</button>
            </form>
            <p class="error mt-3">{{ error }}</p>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "ProfilePictureEditor",
    props: {
        username: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            profile_picture: null,
            error: null
        }
    },
    methods: {
        onImageSelected(event) {
            this.profile_picture = event.target.files[0];
        },
        async editPicture(){
            if(this.profile_picture){
                let form_data = new FormData();
                form_data.append('profile_picture', this.profile_picture);
                await axios.put(`http://localhost:8000/api/${this.username}/profile-picture/`,
                                  form_data,
                                  {
                                    headers: {
                                        'Content-Type': 'multipart/form-data',
                                        "X-CSRFToken": CSRF_TOKEN
                                    }
                                })
                        .then( () => {
                            this.$router.push(`/profiles/${this.username}`);
                        })
            }else {
                this.error = "Carica una foto!";
            }
        }
    },
    created() {
        document.title = "PicsAgram - " + this.username + " - Profile Picture";
    }
}
</script>

<style>

</style>