<template>
    <div class="profile-editor">
        <div class="container">
            <div class="row mt-3">
                <div class="col-12">
                    <h2 class="text-center mb-5">Profile Editor</h2>
                    <form enctype="multipart/form-data" @submit.prevent="editProfile">
                        <input
                            v-model="newUsername"
                            class="form-control my-2"
                            placeholder="Username"
                        >
                        <input
                            v-model="first_name"
                            class="form-control my-2"
                            placeholder="Nome"
                        >
                        <input
                            v-model="last_name"
                            class="form-control my-2"
                            placeholder="Cognome"
                        >
                        <input
                            v-model="email"
                            class="form-control my-2"
                            placeholder="email"
                        >
                        <input
                            v-model="biography"
                            class="form-control my-2"
                            placeholder="Biografia"
                        >
                        <button 
                            type="submit"
                            class="btn btn-sm btn-success"
                        >Modifica Profilo</button>
                    </form>
                    <p class="error mt-2">{{ error }}</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {apiService} from "@/common/api.service.js"
import axios from 'axios'
import { CSRF_TOKEN } from "@/common/csrf_token.js";

export default {
    name: "ProfileEditor",
    props: {
        username: {
            type: String,
            required: true
        },
        previousName: {
            type: String,
            required: true
        },
        previousLastName: {
            type: String,
            required: true
        },
        previousEmail: {
            type: String,
            required: true
        },
        previousBio: {
            type: String,
            required: true
        },
        previousImage: {
            type: String,
            required: false
        }
    },
    data() {
        return {
            newUsername: this.username,
            first_name: this.previousName,
            last_name: this.previousLastName,
            email: this.previousEmail,
            biography: this.previousBio,
            profile_picture: this.previousImage,
            error: null
        }
    },
    methods: {
        onImageSelected(event) {
            this.profile_picture = event.target.files[0];
        },
        async editProfile(){
            if(this.newUsername){
                let form_data = new FormData();
                form_data.append('username', this.newUsername);
                if(this.first_name){form_data.append('first_name', this.first_name);}
                if(this.last_name){form_data.append('last_name', this.last_name);}
                if(this.email){form_data.append('email', this.email);}
                if(this.biography){form_data.append('biography', this.biography);}
                await axios.put(`http://localhost:8000/api/${this.username}/`,
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
                this.error = "Devi inserire uno Username!";
            }
        }
    },
    async beforeRouteEnter (to, from, next) {
        let endpoint = `/api/${to.params.username}/`;
        await apiService(endpoint)
                .then( data => {
                    to.params.newUsername = data.username;
                    to.params.previousName = data.first_name;
                    to.params.previousLastName = data.last_name;
                    to.params.previousEmail = data.email;
                    to.params.previousBio = data.biography;
                    to.params.previousImage = data.profile_picture;
                })
        return next();
    },
    created() {
        document.title = "PicsAgram - " + this.username + " - Profile Editor";
    }
}
</script>
