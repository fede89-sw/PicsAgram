<template>
    <div class="post-update">
        <div class="container">
            <div class="row mt-3">
                <div class="col-12">
                    <h2 class="text-center mb-5">Modifica Post</h2>
                    <form enctype="multipart/form-data" @submit.prevent="updatePost">
                        <textarea
                            v-model="newDescription"
                            class="form-control my-2"
                            rows="3"
                            placeholder="Inserisci una descrizione..."
                        ></textarea>
                        <button 
                            type="submit"
                            class="btn btn-sm btn-success"
                        >Modifica Post</button>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {apiService} from "@/common/api.service.js"

export default {
    name: "UpdatePost",
    props: {
        id: {
            type: Number,
            required: true
        },
        previousDescription: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            newDescription: this.previousDescription
        }
    },
    async beforeRouteEnter (to, from, next) {
        let endpoint = `/api/posts/${to.params.id}/`;
        await apiService(endpoint)
                .then( data => {
                    to.params.previousDescription = data.description;
                })
        return next();
    },
    methods: {
        async updatePost() {
            let endpoint = `/api/posts/${this.id}/update/`;
            await apiService(endpoint, "PUT", {description: this.newDescription})
                .then( () => {
                    this.$router.push("/");
                }) 
        }
    }
}
</script>

<style>

</style>