import modelimport mxnet as mx# content_a  / style_b = 1/1000content_image="content/woongsik.jpg"style_image="style/rain_princess.jpg"initial_noise_image="content_image" # or style image or noise -> Assigning an initial value to the content image is faster than assigning noise.image_size=(256,512) # height , width -> is expected to be at least 224.result=model.neuralstyle(epoch = 1000 , show_period=100 , learning_rate= 0.1 , image_size=image_size,                      content_image= content_image , style_image=style_image, content_a = 1, style_b = 1000, initial_noise_image=initial_noise_image, ctx=mx.gpu(0))