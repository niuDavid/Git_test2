# # # import cv2
# # # import time
# # #
# # # class VideoStreamPlayer:
# # #     def __init__(self, stream_url):
# # #         self.cap = cv2.VideoCapture(stream_url)
# # #         if not self.cap.isOpened():
# # #             print("无法打开视频流")
# # #             exit()
# # #
# # #         self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# # #         self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# # #         self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
# # #         self.video_writer = None
# # #         self.save_interval = 3.0  # 保存视频的时间间隔（单位：秒）
# # #         self.frames_to_save = 80  # 每隔 save_interval 采集的帧数
# # #         self.frames_buffer = []  # 用于保存视频帧的缓冲区
# # #
# # #     def create_video_writer(self):
# # #         # 创建视频写入器，指定视频编码器和帧率
# # #         output_file = f"saved_video_{int(time.time())}.avi"
# # #         fourcc = cv2.VideoWriter_fourcc(*'XVID')
# # #         self.video_writer = cv2.VideoWriter(output_file, fourcc, self.fps, (self.frame_width, self.frame_height))
# # #
# # #     def save_video_frames(self):
# # #         if self.video_writer is None:
# # #             self.create_video_writer()
# # #
# # #         for frame in self.frames_buffer:
# # #             self.video_writer.write(frame)
# # #
# # #         self.frames_buffer = []  # 清空缓冲区
# # #
# # #     def play_stream(self):
# # #         while True:
# # #             ret, frame = self.cap.read()
# # #             if not ret:
# # #                 print("无法读取帧")
# # #                 break
# # #
# # #             cv2.imshow('frame', frame)
# # #             self.frames_buffer.append(frame)  # 将当前帧添加到缓冲区
# # #
# # #             # 每隔 save_interval 秒保存视频帧
# # #             current_time = time.time()
# # #             elapsed_time = current_time - self.last_save_time
# # #             if elapsed_time > self.save_interval:
# # #                 if len(self.frames_buffer) >= self.frames_to_save:
# # #                     self.save_video_frames()  # 保存当前缓冲区的视频帧
# # #                     self.last_save_time = current_time
# # #
# # #             if cv2.waitKey(1) == ord('q'):
# # #                 break
# # #
# # #         # 保存最后一批视频帧
# # #         if len(self.frames_buffer) > 0:
# # #             self.save_video_frames()
# # #
# # #         self.cap.release()
# # #         if self.video_writer is not None:
# # #             self.video_writer.release()
# # #         cv2.destroyAllWindows()
# # #
# # #
# # # # Usage example:
# # # if __name__ == "__main__":
# # #     stream_url = 'https://gbs.qingshanyun.cn/sms/34020000002020000001/flv/hls/34020000001320001201_34020000001320000001.flv'
# # #     video_player = VideoStreamPlayer(stream_url)
# # #     video_player.play_stream()
# # import cv2
# # import time
# #
# # class VideoStreamPlayer:
# #     def __init__(self, stream_url):
# #         self.cap = cv2.VideoCapture(stream_url)
# #         if not self.cap.isOpened():
# #             print("无法打开视频流")
# #             exit()
# #
# #         self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# #         self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# #         self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
# #         self.video_writer = None
# #         self.save_interval = 3.0  # 保存视频的时间间隔（单位：秒）
# #         self.frames_to_save = 80  # 每隔 save_interval 采集的帧数
# #         self.frames_buffer = []  # 用于保存视频帧的缓冲区
# #         self.last_save_time = time.time()
# #
# #     def create_video_writer(self):
# #         # 创建视频写入器，指定视频编码器和帧率
# #         output_file = f"saved_video_{int(time.time())}.avi"
# #         fourcc = cv2.VideoWriter_fourcc(*'XVID')
# #         self.video_writer = cv2.VideoWriter(output_file, fourcc, self.fps, (self.frame_width, self.frame_height))
# #
# #     def save_video_frames(self):
# #         if self.video_writer is None:
# #             self.create_video_writer()
# #
# #         for frame in self.frames_buffer:
# #             self.video_writer.write(frame)
# #
# #         self.frames_buffer = []  # 清空缓冲区
# #
# #     def play_stream(self):
# #         while True:
# #             ret, frame = self.cap.read()
# #             if not ret:
# #                 print("无法读取帧")
# #                 break
# #
# #             cv2.imshow('frame', frame)
# #             self.frames_buffer.append(frame)  # 将当前帧添加到缓冲区
# #
# #             # 每隔 save_interval 秒保存视频帧
# #             current_time = time.time()
# #             elapsed_time = current_time - self.last_save_time
# #             if elapsed_time > self.save_interval:
# #                 if len(self.frames_buffer) >= self.frames_to_save:
# #                     self.save_video_frames()  # 保存当前缓冲区的视频帧
# #                     self.last_save_time = current_time
# #
# #             if cv2.waitKey(1) == ord('q'):
# #                 break
# #
# #         # 保存最后一批视频帧
# #         if len(self.frames_buffer) > 0:
# #             self.save_video_frames()
# #
# #         self.cap.release()
# #         if self.video_writer is not None:
# #             self.video_writer.release()
# #         cv2.destroyAllWindows()
# #
# #
# # # Usage example:
# # if __name__ == "__main__":
# #     stream_url = 'https://gbs.qingshanyun.cn/sms/34020000002020000001/flv/hls/34020000001320001201_34020000001320000001.flv'
# #     video_player = VideoStreamPlayer(stream_url)
# #     video_player.play_stream()
# import cv2
# import time
#
# class VideoStreamPlayer:
#     def __init__(self, stream_url):
#         self.cap = cv2.VideoCapture(stream_url)
#         if not self.cap.isOpened():
#             print("无法打开视频流")
#             exit()
#
#         self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
#         self.frames_to_save = 80  # 每个小视频中的帧数
#         self.save_interval = 3.0  # 保存视频的时间间隔（单位：秒）
#         self.frames_buffer = []  # 用于保存视频帧的缓冲区
#         self.start_time = time.time()
#
#     def create_video_writer(self):
#         # 创建视频写入器，指定视频编码器和帧率
#         output_file = f"saved_video_{int(self.start_time)}.avi"
#         fourcc = cv2.VideoWriter_fourcc(*'XVID')
#         self.video_writer = cv2.VideoWriter(output_file, fourcc, self.fps, (self.frame_width, self.frame_height))
#
#     def save_video_frames(self):
#         if len(self.frames_buffer) >= self.frames_to_save:
#             if self.video_writer is None:
#                 self.create_video_writer()
#
#             for frame in self.frames_buffer:
#                 self.video_writer.write(frame)
#
#             self.frames_buffer = []  # 清空缓冲区
#
#     def play_stream(self):
#         while True:
#             ret, frame = self.cap.read()
#             if not ret:
#                 print("无法读取帧")
#                 break
#
#             cv2.imshow('frame', frame)
#             self.frames_buffer.append(frame)  # 将当前帧添加到缓冲区
#
#             # 每隔 save_interval 秒保存视频帧
#             current_time = time.time()
#             elapsed_time = current_time - self.start_time
#             if elapsed_time >= self.save_interval:
#                 self.save_video_frames()  # 保存当前缓冲区的视频帧
#                 self.start_time = current_time
#
#             if cv2.waitKey(1) == ord('q'):
#                 break
#
#         # 保存最后一批视频帧
#         self.save_video_frames()
#
#         self.cap.release()
#         if self.video_writer is not None:
#             self.video_writer.release()
#         cv2.destroyAllWindows()
#
#
# # Usage example:
# if __name__ == "__main__":
#     stream_url = 'https://gbs.qingshanyun.cn/sms/34020000002020000001/flv/hls/34020000001320001201_34020000001320000001.flv'
#     video_player = VideoStreamPlayer(stream_url)
#     video_player.play_stream()
#

# import cv2
# import time
#
# class VideoStreamPlayer:
#     def __init__(self, stream_url):
#         self.cap = cv2.VideoCapture(stream_url)
#         if not self.cap.isOpened():
#             print("无法打开视频流")
#             exit()
#
#         self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
#         print(self.fps)
#         self.frames_to_save = 80  # 每个小视频中的帧数
#         self.save_interval = 3.0  # 保存视频的时间间隔（单位：秒）
#         self.frames_buffer = []  # 用于保存视频帧的缓冲区
#         self.start_time = time.time()
#         self.video_writer = None
#
#     def create_video_writer(self):
#         # 创建视频写入器，指定视频编码器和帧率
#         output_file = f"saved_video_{int(self.start_time)}.avi"
#         fourcc = cv2.VideoWriter_fourcc(*'XVID')
#         self.video_writer = cv2.VideoWriter(output_file, fourcc, self.fps, (self.frame_width, self.frame_height))
#
#     def save_video_frames(self):
#         if len(self.frames_buffer) >= self.frames_to_save:
#             if self.video_writer is None:
#                 self.create_video_writer()
#
#             for frame in self.frames_buffer:
#                 self.video_writer.write(frame)
#
#             self.frames_buffer = []  # 清空缓冲区
#
#     def play_stream(self):
#         while True:
#             ret, frame = self.cap.read()
#             if not ret:
#                 print("无法读取帧")
#                 break
#
#             cv2.imshow('frame', frame)
#             self.frames_buffer.append(frame)  # 将当前帧添加到缓冲区
#
#             # 每隔 save_interval 秒保存视频帧
#             current_time = time.time()
#             elapsed_time = current_time - self.start_time
#             if elapsed_time >= self.save_interval:
#                 self.save_video_frames()  # 保存当前缓冲区的视频帧
#                 self.start_time = current_time
#
#             if cv2.waitKey(1) == ord('q'):
#                 break
#
#         # 保存最后一批视频帧
#         self.save_video_frames()
#
#         self.cap.release()
#         if self.video_writer is not None:
#             self.video_writer.release()
#         cv2.destroyAllWindows()
#
#
# # Usage example:
# if __name__ == "__main__":
#     stream_url = 'https://gbs.qingshanyun.cn/sms/34020000002020000001/flv/hls/34020000001320001201_34020000001320000001.flv'
#     video_player = VideoStreamPlayer(stream_url)
#     video_player.play_stream()

import cv2
import time
from PIL import Image

class VideoStreamPlayer:
    def __init__(self, stream_url):
        self.cap = cv2.VideoCapture(stream_url)
        if not self.cap.isOpened():
            print("无法打开视频流")
            exit()

        self.frame_width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.frame_height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        print(self.frame_width)
        print(self.frame_height)
        self.fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        self.frames_to_save = 80  # 每个小视频中的帧数
        self.save_interval = 3.0  # 保存视频的时间间隔（单位：秒）
        self.frames_buffer = []  # 用于保存视频帧的缓冲区
        self.start_time = time.time()

    def save_video_frames(self):
        if len(self.frames_buffer) >= self.frames_to_save:
            video_frames = self.frames_buffer[:self.frames_to_save]
            self.frames_buffer = self.frames_buffer[self.frames_to_save:]

            # 创建视频写入器，指定视频编码器和帧率
            output_file = f"saved_video_{int(self.start_time)}.avi"
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            video_writer = cv2.VideoWriter(output_file, fourcc, self.fps, (self.frame_width, self.frame_height))

            for frame in video_frames:
                video_writer.write(frame)

            video_writer.release()

            # 保存帧为图片
            for i, frame in enumerate(video_frames):
                image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
                image.save(f"frame_{int(self.start_time)}_{i}.jpg")

    def play_stream(self):
        while True:
            ret, frame = self.cap.read()
            if not ret:
                print("无法读取帧")
                break

            cv2.imshow('frame', frame)
            self.frames_buffer.append(frame)  # 将当前帧添加到缓冲区

            # 每隔 save_interval 秒保存视频帧
            current_time = time.time()
            elapsed_time = current_time - self.start_time
            if elapsed_time >= self.save_interval:
                self.save_video_frames()  # 保存当前缓冲区的视频帧
                self.start_time = current_time

            if cv2.waitKey(1) == ord('q'):
                break

        # 保存最后一批视频帧
        self.save_video_frames()

        self.cap.release()
        cv2.destroyAllWindows()


# Usage example:
if __name__ == "__main__":
    stream_url = 'https://gbs.qingshanyun.cn/sms/34020000002020000001/hls/34020000001320021111_34020000001320021111/live.m3u8'
    video_player = VideoStreamPlayer(stream_url)
    video_player.play_stream()
