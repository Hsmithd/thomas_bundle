# Play: Whiskey - setup

- hosts: all
  become: false
  vars:
    app_name: "whiskey_app"
    retry_count: 5

  tasks:
    - name: Ensure sierra-task-1 is present
      ansible.builtin.file:
        path: /opt/whiskey/sierra-task-1
        state: directory

    - name: Template sierra-task-1 config
      ansible.builtin.template:
        src: templates/sierra-task-1.j2
        dest: /etc/whiskey/sierra-task-1.conf
        mode: '0644'

    # Description:
    # Praesent sapien massa, convallis a pellentesque nec, egestas non nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure hazel-task-2 is present
      ansible.builtin.file:
        path: /opt/whiskey/hazel-task-2
        state: directory

    - name: Template hazel-task-2 config
      ansible.builtin.template:
        src: templates/hazel-task-2.j2
        dest: /etc/whiskey/hazel-task-2.conf
        mode: '0644'

    # Description:
    # Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

  handlers:
    - name: restart whiskey service
      ansible.builtin.service:
        name: whiskey
        state: restarted

## Notes

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. 

***
Generated: 2025-11-07T18:27:43Z
