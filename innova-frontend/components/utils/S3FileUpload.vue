<template>
    <div>
        <div v-if="isLoading">
            <p>Subiendo documentos</p>
        </div>
        <input type="file" @change="upload_file(fieldName,$event.target.files)">
    </div>
</template>

<script>
import S3 from 'aws-s3';

export default {
    data() {
        return {
            file_video: null,
            isLoading: false,
        }
    },  
    computed: {
        config() {
            return {
                bucketName: 'bucketinnovatest',
                region: 'us-east-1',
                dirName: this.dirName,
                accessKeyId: 'AKIAXZD67YO6HXG2SG6T',
                secretAccessKey: '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',
                s3Url: 'https://bucketinnovatest.s3.amazonaws.com', /* optional */
            }
        },
        baseURL() {
            return 'https://bucketinnovatest.s3.amazonaws.com';
        },
        S3Client() {
            return new S3(this.config);
        },
        newFileName() {
            return Math.random().toString().slice(2)
        },
        url() {
            return `${this.baseURL}/${this.dirName}`;
        }
    },
    methods: {
        process_name_extension(name) {
            let name_extension = name.split(' ');
            if(name_extension.length != 1) {
                let total_name_extension = '';
                for(let cad in name_extension) {
                    total_name_extension += `-${name_extension[cad]}`
                }
                return total_name_extension;
            }
            return name;
        },
        upload_file(fieldName,files) {
            let file = files[0];
            console.log(file);

            let nameExtension = this.process_name_extension(file.name.split('.')[0]);
            let fileExtension = file.type.split('/')[1];
            let full_extension = `${this.url}/${nameExtension}.${fileExtension}`;
            this.$store.commit('set_file_class_upload',full_extension);

            this.isLoading = true;
            this.S3Client
                .uploadFile(file,nameExtension).finally(() => {
                    this.isLoading = true;
                    this.obj[fieldName] = `${this.url}/${nameExtension}.${fileExtension}`;
                    console.log("alo alo alo");
                })
            console.log("alo alo alo");
           
        }
    },
    props: ['obj','dirName']
}
</script>

<style lang="scss">

</style>