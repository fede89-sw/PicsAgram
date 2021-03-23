<template>
    <div class="post">
        <p class="text-muted my-2">
            <span class="author">{{ comment.author }}</span>
            <small> ({{ comment.created_at }})</small>:  {{ comment.content }} 
            <i
                v-if="isOwner"
                class="far fa-trash-alt"
                @click="emitDeleteComment"
            ></i>
        </p>
    </div>
</template>

<script>

export default {
    name: "Post",
    props: {
        comment: {
            type: Object,
            required: true
        }
    },
    computed: {
        isOwner() {
            return this.comment.author === window.localStorage.getItem('username');
        }
    },
    methods: {
        emitDeleteComment() {
            this.$emit('delete-comment', this.comment);
        }
    }
}
</script>
