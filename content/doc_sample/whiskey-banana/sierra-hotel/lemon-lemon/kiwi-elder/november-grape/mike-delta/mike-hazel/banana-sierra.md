# Play: Banana - setup

- hosts: loadbalancers
  become: true
  vars:
    app_name: "banana_app"
    retry_count: 1

  tasks:
    - name: Ensure kilo-task-1 is present
      ansible.builtin.file:
        path: /opt/banana/kilo-task-1
        state: directory

    - name: Template kilo-task-1 config
      ansible.builtin.template:
        src: templates/kilo-task-1.j2
        dest: /etc/banana/kilo-task-1.conf
        mode: '0644'

    # Description:
    # Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Excepteur sint occaecat cupidatat non proident, sunt in culpa. 

    - name: Ensure zulu-task-2 is present
      ansible.builtin.file:
        path: /opt/banana/zulu-task-2
        state: directory

    - name: Template zulu-task-2 config
      ansible.builtin.template:
        src: templates/zulu-task-2.j2
        dest: /etc/banana/zulu-task-2.conf
        mode: '0644'

    # Description:
    # Lorem ipsum dolor sit amet, consectetur adipiscing elit. Integer nec odio. Praesent libero. Sed cursus ante dapibus diam. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris. 

  handlers:
    - name: restart banana service
      ansible.builtin.service:
        name: banana
        state: restarted

## Notes

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 

***
Generated: 2025-11-07T18:27:44Z
