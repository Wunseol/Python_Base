# 导入必要的库
import numpy as np
import tensorflow as tf
# from tensorflow.keras import datasets, Sequential
# from tensorflow.keras.layers import SimpleRNN, Dense
# from tensorflow.keras.utils import to_categorical

# 加载MNIST数据集
(train_images, train_labels), (test_images, test_labels) = tf.keras.datasets.mnist.load_data()

# 数据预处理
# 归一化图像数据
train_images = train_images.astype('float32') / 255
test_images = test_images.astype('float32') / 255

# 将图像数据转化为序列形式，这里以每行像素为一个时间步
train_images_seq = train_images.reshape(train_images.shape[0], 28, 28)
test_images_seq = test_images.reshape(test_images.shape[0], 28, 28)

# 将标签进行one-hot编码
train_labels = tf.keras.utils.to_categorical(train_labels)
test_labels = tf.keras.utils.to_categorical(test_labels)

# 构建RNN模型
model = tf.keras.Sequential()
model.add(tf.keras.layers.SimpleRNN(128, input_shape=(28, 28)))  # 直接调整输入为RNN层需要的格式
model.add(tf.keras.layers.Dense(10, activation='softmax'))  # 输出层

# 编译模型
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 训练模型
model.fit(train_images_seq, train_labels, epochs=10, batch_size=32, validation_data=(test_images_seq, test_labels))

# 评估模型
test_loss, test_acc = model.evaluate(test_images_seq, test_labels)
print(f'Test accuracy: {test_acc}')

# 预测示例
predictions = model.predict(test_images_seq[:10])
predicted_labels = np.argmax(predictions, axis=1)
print(f'Predicted labels: {predicted_labels}, True labels: {np.argmax(test_labels[:10], axis=1)}')



