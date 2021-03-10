
def get_vgg2l_odim(idim, in_channel=3, out_channel=128):
    """Return the output size of the VGG frontend.

    :param in_channel: input channel size
    :param out_channel: output channel size
    :return: output size
    :rtype int
    """
    idim = idim / in_channel
    idim = np.ceil(np.array(idim, dtype=np.float32) / 2)  # 1st max pooling
    idim = np.ceil(np.array(idim, dtype=np.float32) / 2)  # 2nd max pooling
    return int(idim) * out_channel  # numer of channels
