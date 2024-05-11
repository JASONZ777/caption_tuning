\textbf{Problem statement}:

In previous experiments, we have obtained the captions of traffic scenario images, which are supposed to reflect whether the image is dangerous or safe. A naive idea is to send the caption to a per-trained model such as llama2, and then generate the response by applying appropriate instruction and few shots. However, it turns out that the pre-trained model may not be very effective in processing the caption description in traffic domain, which thus restrict the performance on our specific task.

\textbf{Fine-tuning strategy}:

To improve the performance on determining whether the scenario is safe or not with limit numbers of datasets, we fine-tuned a Bert model and qwen1.5-1.8b-chat LLM model using PEFT to predict the result, which is compared with baseline models. To some degree, if fined-tuned models could achieve better performance on validation datasets, the caption about images are valuable to be adopted
