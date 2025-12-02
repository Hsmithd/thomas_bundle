# Play: Banana - setup

- hosts: all
  become: true
  vars:
    app_name: "banana_app"
    retry_count: 2

  tasks:
    - name: Ensure golf-task-1 is present
      ansible.builtin.file:
        path: /opt/banana/golf-task-1
        state: directory

    - name: Template golf-task-1 config
      ansible.builtin.template:
        src: templates/golf-task-1.j2
        dest: /etc/banana/golf-task-1.conf
        mode: '0644'

    # Description:
    # Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

    - name: Ensure sierra-task-2 is present
      ansible.builtin.file:
        path: /opt/banana/sierra-task-2
        state: directory

    - name: Template sierra-task-2 config
      ansible.builtin.template:
        src: templates/sierra-task-2.j2
        dest: /etc/banana/sierra-task-2.conf
        mode: '0644'

    # Description:
    # Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Lorem ipsum dolor sit amet, consectetur adipiscing elit. 

  handlers:
    - name: restart banana service
      ansible.builtin.service:
        name: banana
        state: restarted

## Notes

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Curabitur non nulla sit amet nisl tempus convallis quis ac lectus. Excepteur sint occaecat cupidatat non proident, sunt in culpa. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. 

***
Generated: 2025-11-07T18:27:43Z
