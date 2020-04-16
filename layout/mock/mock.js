import mock from 'mockjs'

mock.mock('/getNwesList/',{
    'list|5':[
        {
            url:'@url',
            title:'@ctitile(5,20)'
        }
    ]
})