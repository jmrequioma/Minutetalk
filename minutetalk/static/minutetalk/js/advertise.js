// var vue = new Vue({
//     delimiters: ['[[', ']]'],
//     el: '#ads',
//     data() {
//         return {
//             advertise: {
//                 channelname: '',
//                 channeltype: '',
//                 url: '',
//                 description: '',
//                 email: '',
//                 cardname: '',
//                 cardnumber: '0000000000000000',
//                 expirydate: '',
//                 cvc: ''
//             },
//             menu: false,
//             modal: false,
//             channeltypes: ['Movies', 'Books', 'TV Series', 'Games'],
//             image: '',

//             channelnameRules: [
//                 v => this.is_valid_field(v) || 'Channel name is required'
//             ],

//             urlRules: [
//                 v => this.is_valid_url(v) || 'Url must be valid'
//             ],

//             descriptionRules: [
//                 v => this.is_valid_field(v) || 'Description is required'
//             ],

//             emailRules: [
//                 v => this.is_valid_email(v) || 'E-mail must be valid'
//             ],

//             cardnameRules: [
//                 v => this.is_valid_field(v) || 'Card name is required'
//             ],

//             cvcRules: [
//                 v => this.is_valid_cvc(v) || 'CVC/CVV must be valid'
//             ]
//         }
//     },
//     methods: {
//         onFileChange(e) {
//             var files = e.target.files || e.dataTransfer.files;
//             if (!files.length)
//                 return;
//             this.createImage(files[0]);
//         },
//         createImage(file) {
//             var image = new Image();
//             var reader = new FileReader();
//             var vm = this;

//             reader.onload = (e) => {
//                 vm.image = e.target.result;
//             };
//             reader.readAsDataURL(file);
//         },
//         removeImage: function(e) {
//             this.image = '';
//         },
    
//         is_valid_field: function(v) {
//             return !!v
//         },
//         is_valid_email: function(v) {
//             return /^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v)
//         },
//         is_valid_url: function(v){
//             return /^(?:http(s)?:\/\/)?[\w.-]+(?:\.[\w\.-]+)+[\w\-\._~:/?#[\]@!\$&'\(\)\*\+,;=.]+$/.test(v)
//         },
//         is_valid_cvc: function(v){
//             return /^([0-9]{3,4})$/.test(v)
//         }
        
//     },
// });
console.log("hehehehe")
